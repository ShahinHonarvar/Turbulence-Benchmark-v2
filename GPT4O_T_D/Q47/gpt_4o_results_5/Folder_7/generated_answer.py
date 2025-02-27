def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    filtered_string = ''.join(filter(str.isalpha, s[119:257]))
    result = set()
    for length in range(104, 124):
        for i in range(len(filtered_string) - length + 1):
            substring = filtered_string[i:i + length]
            if is_palindrome(substring):
                result.add(substring)
    return result