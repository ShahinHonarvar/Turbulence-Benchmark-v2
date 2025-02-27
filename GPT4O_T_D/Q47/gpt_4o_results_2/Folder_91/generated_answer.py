def palindromes_of_specific_lengths(s):

    def is_palindrome_substring(sub):
        return sub.lower() == sub[::-1].lower() and len(sub) in {3, 4, 5}
    s = s[:11]
    english_letters = ''.join((c for c in s if c.isalpha()))
    results = set()
    for start in range(len(english_letters)):
        for end in range(start + 3, min(start + 6, len(english_letters) + 1)):
            substring = english_letters[start:end]
            if is_palindrome_substring(substring):
                results.add(substring.lower())
    return results