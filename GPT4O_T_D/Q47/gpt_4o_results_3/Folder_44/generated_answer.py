def palindromes_of_specific_lengths(s):
    start_index = 18
    end_index = 98
    min_length = 31
    max_length = 51
    substring = s[start_index:end_index + 1]
    palindrome_set = set()
    allowed_chars = set('abcdefghijklmnopqrstuvwxyz')
    for i in range(len(substring) - min_length + 1):
        for j in range(min_length, max_length + 1):
            if i + j > len(substring):
                break
            segment = ''.join([c for c in substring[i:i + j].lower() if c in allowed_chars])
            if len(segment) >= min_length and segment == segment[::-1]:
                palindrome_set.add(segment)
    return palindrome_set