from itertools import permutations

def palindromes_between_indices(string):
    index_1_to_7 = string[1:8]
    palindromes_of_length_5 = set()
    for p in permutations(index_1_to_7):
        string_created = ''.join(p).lower()
        for i in range(len(string_created) - 4):
            palindrome = string_created[i:i + 5]
            if palindrome == palindrome[::-1]:
                palindromes_of_length_5.add(palindrome)
    return palindromes_of_length_5