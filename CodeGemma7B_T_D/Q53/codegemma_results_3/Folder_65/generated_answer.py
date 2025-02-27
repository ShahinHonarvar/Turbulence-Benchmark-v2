from collections import defaultdict

def palindrome_of_length_at_least_n(some_str):
    some_str = some_str.lower()
    palindrome = defaultdict(set)
    for i in range(len(some_str)):
        for j in range(i + 1, len(some_str)):
            if some_str[i:j + 1] == some_str[i:j + 1][::-1]:
                palindrome[j - i + 1].add(some_str[i:j + 1])
    result = {k: v for k, v in palindrome.items() if k >= 15}
    return result