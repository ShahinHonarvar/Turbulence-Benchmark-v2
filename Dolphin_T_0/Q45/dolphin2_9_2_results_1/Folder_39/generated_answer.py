def palindromes_between_indices(string):
    substring = string[2:6].lower()
    return {x for i in range(len(substring)) for x in set(substring[i:]) & set(substring[:i]) if len(x) >= 3}