from collections import defaultdict
from collections import Counter

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    char_counts = defaultdict(int)
    for char in string:
        char_counts[char] += 1
    all_palindromes = []
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1]:
                all_palindromes.append(substring)
    filtered_palindromes = []
    for palindrome in all_palindromes:
        if len(palindrome) >= 4:
            filtered_palindromes.append(palindrome)
    return set(filtered_palindromes)