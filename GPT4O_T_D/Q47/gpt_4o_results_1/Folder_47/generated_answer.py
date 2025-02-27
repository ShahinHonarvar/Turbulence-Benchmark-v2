def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[39:95]
    s = ''.join(filter(str.isalpha, s)).lower()
    results = set()
    for length in range(14, 53):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if is_palindrome(substring):
                results.add(substring)
    return results