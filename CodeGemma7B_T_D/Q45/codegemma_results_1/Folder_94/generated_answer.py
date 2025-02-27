def palindromes_between_indices(str):
    Complete_str = str[3:5].lower()
    if Complete_str == Complete_str[::-1]:
        list = set(Complete_str)
        return list
    else:
        return set()