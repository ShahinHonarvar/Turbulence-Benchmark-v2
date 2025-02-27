def palindromes_between_indices(string):
    letters = [string[i].lower() for i in range(2, 10) if string[i].isalpha()]
    if len(set(letters)) < 2:
        return set()
    return {''.join(per) for per in permutations(letters, len(letters)) if per == per[::-1]}