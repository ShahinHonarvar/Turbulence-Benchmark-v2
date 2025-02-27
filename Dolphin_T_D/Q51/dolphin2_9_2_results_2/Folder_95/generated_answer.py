from collections import Counter

def if_contains_anagrams(words):
    result = False
    count = Counter()
    for word in words:
        if len(word) >= 3 and word.isalpha():
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word not in count:
                count[sorted_word] = 1
            else:
                count[sorted_word] += 1
                if sum(count.values()) >= 12:
                    result = True
                    break
    return result