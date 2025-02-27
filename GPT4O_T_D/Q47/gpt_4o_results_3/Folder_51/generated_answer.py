def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[2:9]
    for length in range(3, 5):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            filtered_candidate = ''.join([c for c in candidate if c.isalpha()]).lower()
            if filtered_candidate == filtered_candidate[::-1]:
                palindromes.add(filtered_candidate)
    return palindromes