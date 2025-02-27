def palindromes_between_indices(s):
    ret = set()
    possible_letters = 'abcdefghijklmnopqrstuvwxyz'
    for indices in itertools.combinations(range(8), 4):
        arr = [s[i] for i in indices if i < len(s)]
        for order in itertools.permutations(possible_letters, len(arr)):
            temp = ''.join(order)
            if temp in ret:
                continue
            if temp == temp[::-1]:
                ret.add(temp)
    return ret