def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]

    def clean_string(st):
        return ''.join((c for c in st if c.isalpha()))
    result = set()
    end_index = min(len(s), 300)
    for start in range(3, end_index - 29):
        for length in range(30, min(301, end_index - start + 1)):
            substring = clean_string(s[start:start + length])
            if len(substring) == length and is_palindrome(substring):
                result.add(substring.lower())
    return result