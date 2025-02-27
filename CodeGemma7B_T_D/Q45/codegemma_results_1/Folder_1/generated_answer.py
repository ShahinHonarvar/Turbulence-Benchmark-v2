from itertools import permutations

def palindromes_between_indices(text):
    english_upper = set(range(ord('A'), ord('Z') + 1))
    pos = (4, 5, 6, 7)
    answer = set()
    for permutation in permutations(english_upper, 4):
        check = True
        temp = text[pos[0]:pos[1] + 1] + text[pos[2]:pos[3] + 1]
        for i in range(len(temp)):
            if ord(temp[i]) - ord(permutation[i]) not in range(20):
                check = False
                break
        if check:
            answer.add(''.join(permutation))
    return answer