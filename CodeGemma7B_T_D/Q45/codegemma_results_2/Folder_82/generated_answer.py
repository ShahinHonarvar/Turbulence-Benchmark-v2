def palindromes_between_indices(text):
    used = {char.lower() for char in text[1:7] if char.isalpha()}
    if len(used) < 7:
        return set()
    result = set()
    for perm in itertools.product(used, repeat=7):
        perm_list = list(perm)
        perm_list.sort()
        palindrome = ''.join(perm_list)
        result.add(palindrome)
    return result