def palindromes_of_specific_lengths(s):
    substring = s[119:256]
    palindromes = set()
    for length in range(104, 124):
        for start_index in range(len(substring) - length + 1):
            sub = substring[start_index:start_index + length]
            if all((c.isalpha() for c in sub)) and sub.lower() == sub[::-1].lower():
                palindromes.add(sub)
    return palindromes