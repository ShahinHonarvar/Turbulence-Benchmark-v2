from itertools import combinations

def palindrome_of_length_at_least_n(a_string):
    palindrome_set = set()
    a_string = a_string.lower()
    for i in range(29, len(a_string) + 1):
        for combo in combinations(range(len(a_string)), i):
            sub_string = [a_string[j] for j in combo]
            sub_string = ''.join(sub_string)
            if sub_string == sub_string[::-1] and sub_string.isalpha():
                palindrome_set.add(sub_string)
    return palindrome_set