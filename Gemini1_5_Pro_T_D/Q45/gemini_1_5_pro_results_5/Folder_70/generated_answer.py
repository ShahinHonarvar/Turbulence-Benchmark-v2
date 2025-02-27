import re
  from collections import Counter

def palindromes_between_indices(string):
    letters = re.sub('[^a-z]', '', string[1:7].lower())
    counts = Counter(letters)
    pals = set()
    if len(letters) >= 4:

        def generate_palindromes(prefix, odd_count):
            if len(prefix) >= 4:
                pals.add(prefix)
            for letter, count in counts.items():
                if count >= 2:
                    counts[letter] -= 2
                    generate_palindromes(letter + prefix + letter, odd_count)
                    counts[letter] += 2
                elif odd_count == 0:
                    counts[letter] -= 1
                    generate_palindromes(letter + prefix + letter, odd_count + 1)
                    counts[letter] += 1
        generate_palindromes('', 0)
    return pals