def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    result = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    segment = s[14:91]
    for length in range(55, 72):
        for i in range(len(segment) - length + 1):
            substring = segment[i:i + length]
            if is_palindrome(substring):
                result.add(substring)
    return result