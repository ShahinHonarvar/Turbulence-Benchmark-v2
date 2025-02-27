def palindromes_between_indices(input_string):
    subs_string = input_string[0:8]
    subs_string = subs_string.lower()
    palindromes = set()
    for i in range(4, len(subs_string) + 1):
        for j in range(len(subs_string) - i + 1):
            sub = subs_string[j:j + i]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes