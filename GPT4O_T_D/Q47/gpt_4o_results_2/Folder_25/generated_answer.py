def palindromes_of_specific_lengths(s):

    def is_palindrome(chars):
        return chars == chars[::-1]
    start, end = (26, 84)
    valid_palindromes = set()
    filtered_string = ''.join([c.lower() for c in s[start:end + 1] if c.isalpha()])
    for length in range(30, 47):
        for i in range(len(filtered_string) - length + 1):
            substring = filtered_string[i:i + length]
            if is_palindrome(substring):
                valid_palindromes.add(substring)
    return valid_palindromes