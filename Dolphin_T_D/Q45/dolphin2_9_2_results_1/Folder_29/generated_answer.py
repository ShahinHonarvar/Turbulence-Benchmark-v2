def palindromes_between_indices(s):
    s = s[2:10]
    s = ''.join([ch for ch in s if ch.isalpha()])
    palindromes = set()
    for length in range(6, len(s) + 1):
        for start_index in range(len(s) - length + 1):
            sub = s[start_index:start_index + length]
            sub = ''.join([ch.lower() for ch in sub])
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes