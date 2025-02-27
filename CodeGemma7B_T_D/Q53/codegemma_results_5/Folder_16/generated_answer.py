from collections import defaultdict

def palindrome_of_length_at_least_n(text):
    palindromes = defaultdict(set)
    twoletter = defaultdict(set)
    for letter in text.lower():
        if letter.isalpha():
            oneletter = letter.lower()
            twoletter[oneletter].add(oneletter)
            left, right = (letter, letter)
            while left >= 'a' and right <= 'z' and (text[left] == text[right]):
                palindrome = ''.join(text[left:right + 1])
                if len(palindrome) >= 119 and palindrome not in palindromes[len(palindrome)]:
                    palindromes[len(palindrome)].add(palindrome)
                left -= 1
                right += 1
            left, right = (letter, letter)
            while left >= 'a' and right <= 'z' and (text[left] == text[right]):
                palindrome = ''.join(text[left:right + 1])
                if len(palindrome) >= 119 and palindrome not in twoletter[letter]:
                    twoletter[letter].add(palindrome)
                left -= 1
                right += 1
    return set().union(*(sets for sets in palindromes.values()))