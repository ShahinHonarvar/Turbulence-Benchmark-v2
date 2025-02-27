import itertools
    from collections import Counter

def palindromes_between_indices(s):

    def is_palindrome(string):
        return string == string[::-1]
    s = s[7:9].lower()
    letters = [i for i in s if i.isalpha()]
    counter = Counter(letters)
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for combo in itertools.combinations_with_replacement(counter.elements(), r):
            if len(set(combo)) <= 1 or (len(set(combo)) == 2 and abs[counter[i] - counter[j]] <= 1):
                palindrome = ''.join(combo)
                if is_palindrome(palindrome):
                    palindromes.add(palindrome)
    return palindromes