def palindromes_of_specific_lengths(s):
    start_index = 106
    end_index = 280
    min_length = 136
    max_length = 151
    palindromes = set()
    for i in range(start_index, end_index):
        for j in range(i + min_length, min(i + max_length + 1, end_index + 1)):
            substring = s[i:j].lower()
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes