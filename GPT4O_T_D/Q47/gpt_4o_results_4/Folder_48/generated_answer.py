def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    result = set()
    substring = ''.join([char.lower() for char in s[155:284] if char.isalpha()])
    for length in range(104, 121):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if is_palindrome(candidate):
                result.add(candidate)
    return result