from collections import defaultdict

def letter_count(string, start, end):
    count = defaultdict(int)
    for i in range(start, end + 1):
        if 0 <= i < len(string) and string[i].isalpha():
            count[string[i].lower()] += 1
    return count

def is_palindrome(count):
    odd_count = sum((1 for v in count.values() if v % 2 != 0))
    return odd_count <= 1

def form_palindromes(count):
    palindromes = set()
    for combination in itertools.product(range(2), repeat=len(count)):
        if sum(combination) % 2 == 0:
            continue
        palindrome = ''
        for letter, freq in count.items():
            palindrome += letter * (combination[0] * 2 + freq % 2)
        if 3 <= len(palindrome) <= 6:
            palindromes.add(palindrome)
    return palindromes

def palindromes_between_indices(string):
    count = letter_count(string, 2, 6)
    palindromes = form_palindromes(count)
    return palindromes