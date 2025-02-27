from itertools import permutations

def palindromes_between_indices(text):
    lst = [i for i in text if i.isalpha()]
    lst = [i.lower() for i in lst if i in 'abcdefghijklmnopqrstuvwxyz']
    answer = set()
    if len(lst) >= 4:
        for i in permutations(lst):
            temp = ''.join(i)
            if temp in answer:
                continue
            if temp[0] == temp[-1] and temp[1] == temp[-2]:
                answer.add(temp)
    return answer