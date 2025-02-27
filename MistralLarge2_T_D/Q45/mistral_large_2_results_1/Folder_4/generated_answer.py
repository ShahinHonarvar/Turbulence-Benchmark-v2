from collections import Counter

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s[3:10]
    filtered_chars = ''.join((c for c in s if c.isalpha()))
    filtered_chars = filtered_chars.lower()
    char_counts = Counter(filtered_chars)
    palindromes = set()
    for length in range(7, len(filtered_chars) + 1):
        for i in range(len(filtered_chars) - length + 1):
            substring = filtered_chars[i:i + length]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes