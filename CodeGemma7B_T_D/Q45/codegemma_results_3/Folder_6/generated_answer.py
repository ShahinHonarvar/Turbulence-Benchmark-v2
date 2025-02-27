import itertools

def palindromes_between_indices(string):
    indices = [i for i in range(8)]
    ascii_lowercase = list(itertools.product(indices, repeat=len(string)))
    lowercase_list = []
    for permutation in ascii_lowercase:
        temp_list = [string[index] for index in permutation]
        lowercase_list.append(''.join(temp_list).lower())
    filtered_list = [palindrome for palindrome in lowercase_list if palindrome.isalnum() and palindrome.islower() and (len(palindrome) >= 4)]
    return set(filtered_list)