import re
from collections import defaultdict

def palindrome_of_length_n(string, n=181):
    string = re.sub('\\W+', '', string).lower()
    if len(string) < n:
        return set()
    table = defaultdict(list)
    for i in range(len(string)):
        for j in range(i, min(len(string), i + n) + 1):
            sub = string[i:j]
            if sub == sub[::-1]:
                table[len(sub)].append(sub)
    return {palindrome for palindrome_length in table if palindrome_length == n for palindrome in table[palindrome_length]}