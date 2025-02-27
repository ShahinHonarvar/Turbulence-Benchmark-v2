def palindromes_between_indices(string):
    substring = string[8:10]
    substring = substring.lower()
    substring = ''.join(sorted(substring))
    result = set()
    for i in range(len(substring)):
        for j in range(i + 2, len(substring) + 1):
            sub = substring[i:j]
            if sub == sub[::-1]:
                result.add(sub)
    if not result:
        return set()
    else:
        return result