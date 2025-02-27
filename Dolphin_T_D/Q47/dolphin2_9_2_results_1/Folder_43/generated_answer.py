def palindromes_of_specific_lengths(s):
    substring = s[41:90]
    lengths = range(23, 39)
    palindromes_set = set()
    for length in lengths:
        for start_index in range(len(substring) - length + 1):
            sub = substring[start_index:start_index + length].lower()
            if sub == sub[::-1]:
                if sub.isalpha():
                    palindromes_set.add(sub)
    return palindromes_set