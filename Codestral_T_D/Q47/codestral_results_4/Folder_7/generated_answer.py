def palindromes_of_specific_lengths(s):
    s = s.lower()
    start_index = 119
    end_index = 256
    min_length = 104
    max_length = 123
    palindromes = set()
    for i in range(start_index, end_index + 1):
        for j in range(min_length, max_length + 1):
            if i + j <= end_index and s[i:i + j] == s[i:i + j][::-1] and s[i:i + j].isalpha():
                palindromes.add(s[i:i + j])
    return palindromes