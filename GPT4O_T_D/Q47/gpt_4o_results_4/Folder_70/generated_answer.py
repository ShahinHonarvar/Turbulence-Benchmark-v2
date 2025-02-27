def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    result = set()
    filtered_string = ''.join([c for c in s[10:71] if c.isalpha()])
    for length in range(24, 53):
        for start in range(len(filtered_string) - length + 1):
            substring = filtered_string[start:start + length]
            if is_palindrome(substring):
                result.add(substring)
    return result