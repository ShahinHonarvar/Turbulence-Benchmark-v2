def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        filtered_sub = ''.join((c.lower() for c in sub if c.isalpha()))
        return filtered_sub == filtered_sub[::-1]
    start_index = 33
    end_index = 85
    min_length = 26
    max_length = 31
    result = set()
    for length in range(min_length, max_length + 1):
        for i in range(start_index, end_index - length + 2):
            substring = s[i:i + length]
            if is_palindrome(substring):
                result.add(substring)
    return result