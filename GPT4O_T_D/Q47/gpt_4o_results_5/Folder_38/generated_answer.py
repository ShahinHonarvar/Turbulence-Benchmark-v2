def palindromes_of_specific_lengths(s):

    def is_palindrome(seq):
        return seq == seq[::-1]
    substr = s[18:88]
    result = set()
    for start in range(len(substr)):
        for end in range(start + 38, min(start + 61, len(substr) + 1)):
            snippet = ''.join(filter(str.isalpha, substr[start:end])).lower()
            if len(snippet) >= 38 and is_palindrome(snippet):
                result.add(snippet)
    return result