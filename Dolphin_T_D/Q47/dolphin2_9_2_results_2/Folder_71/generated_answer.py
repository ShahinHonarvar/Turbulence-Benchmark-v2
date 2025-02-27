def palindromes_of_specific_lengths(s):
    index_range = s[18:66]
    palindromes_set = set()
    for length in range(23, 37):
        for i in range(len(index_range) - length + 1):
            substring = index_range[i:i + length]
            if substring.lower() == substring[::-1].lower():
                palindromes_set.add(substring)
    return palindromes_set