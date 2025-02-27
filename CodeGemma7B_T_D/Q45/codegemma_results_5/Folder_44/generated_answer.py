def palindromes_between_indices(s):
    set_of_palindromes = set()
    valid_letters = {*'abcdefghijklmnopqrstuvwxyz'}
    counter = {*range(10)}
    for i in range(len(s)):
        if s[i] in valid_letters:
            counter[s[i]] += 1
    for i in range(2, 8):
        for subset in itertools.combinations(counter.keys(), i):
            combination = ''.join(sorted(subset))
            set_of_palindromes.add(combination)
            counter[combination] += 1
    return set_of_palindromes