def palindromes_between_indices(string):
    substring = string[1:7]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 3, len(substring)):
            sub = substring[i:j + 1]
            palin = ''.join(sorted(list(sub.lower())))
            if palin == palin[::-1] and len(palin) >= 4:
                palindromes.add(palin)
    return palindromes