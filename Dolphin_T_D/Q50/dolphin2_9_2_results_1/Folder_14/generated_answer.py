from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    for word in lst:
        if len(word) >= 3 and word.lower() == ''.join(sorted(word.lower())):
            word_count = Counter(word.lower())
            for other in lst:
                if len(other) >= 3 and other.lower() != word.lower() and (Counter(other.lower()) == word_count):
                    count += 1
    return count >= 22