def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        sub = ''.join(filter(str.isalpha, sub)).lower()
        return sub == sub[::-1]
    start, end = (16, 60)
    substring = s[start:end + 1]
    result = set()
    for length in range(16, 40):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if is_palindrome(candidate):
                result.add(candidate)
    return result