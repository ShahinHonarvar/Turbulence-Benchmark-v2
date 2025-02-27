from itertools import permutations

def palindromes_between_indices(my_string):
    result = set()
    used = set()
    for i in range(2, 10):
        for j in range(i, 10):
            for k in permutations(my_string[i:j + 1], r=j + 1 - i):
                check = ''.join(k)
                if check not in used and check == check[::-1]:
                    used.add(check)
                    result.add(check)
    return result