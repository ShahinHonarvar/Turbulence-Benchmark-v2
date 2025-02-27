def palindromes_between_indices(s):
    s = s[1:8].lower()
    letters = set()
    for ch in s:
        if ch.isalpha():
            letters.add(ch)
    if len(letters) < 5:
        return set()

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    for length in range(5, len(s) + 1):
        for i in range(len(s) - length + 1):
            word = s[i:i + length]
            if len(set(word)) <= len(letters) and is_palindrome(word):
                palindromes.add(word)
    return palindromes