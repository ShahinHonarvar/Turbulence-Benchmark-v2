from collections import defaultdict
    import string

def palindromes_between_indices(s):
    palindrome_set = set()
    letters = s[4:8].lower()
    letters = ''.join((c for c in letters if c in string.ascii_letters))
    if len(letters) < 4:
        return palindrome_set

    def is_palindrome(word):
        word = word.lower()
        return word == word[::-1]
    char_freq = defaultdict(int)
    for char in letters:
        char_freq[char] += 1
    for freq in char_freq.values():
        if freq % 2 != 0:
            return {}
    even_chars = sum((1 for freq in char_freq.values() if freq % 2 == 0))
    if even_chars < 2:
        return {}
    for i in range(2, even_chars + 1, 2):
        for combination in itertools.combinations_with_replacement(char_freq.keys(), i):
            palindrome = ''.join(combination) + ''.join(reversed(combination))
            if is_palindrome(palindrome) and len(palindrome) >= 4:
                palindrome_set.add(palindrome)
    return palindrome_set