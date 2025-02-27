from itertools import permutations

def palindromes_between_indices(string):
    answer = set()
    length = len(string)
    if length < 6 or string[1:8].lower() != ''.join(sorted(string[1:8].lower())):
        return answer
    for permutation in permutations(string[1:8]):
        palindrome = ''.join(permutation)
        if palindrome[::-1] in answer:
            answer.add(palindrome)
    return answer