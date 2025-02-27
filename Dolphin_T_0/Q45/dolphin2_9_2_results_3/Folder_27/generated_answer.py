from itertools import permutations

def palindromes_between_indices(s):
    en_let = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
    sub_s = s[2:9]
    length = len(sub_s)
    palidromes = set()
    j = 0
    while j < length:
        possible = set()
        for ele in en_let:
            if ele in sub_s:
                possible.add(ele)
        for perm in permutations(possible, length):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palidromes.add(palindrome)
        j += 1
    return palidromes