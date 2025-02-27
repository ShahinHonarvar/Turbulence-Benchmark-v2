def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:7]]
    unique_letters = list(set(letters))
    n = len(unique_letters)
    palindromes = set()
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                subsring = unique_letters[i] + unique_letters[j] + unique_letters[k]
                if subsring == subsring[::-1]:
                    palindromes.add(subsring)
    return palindromes