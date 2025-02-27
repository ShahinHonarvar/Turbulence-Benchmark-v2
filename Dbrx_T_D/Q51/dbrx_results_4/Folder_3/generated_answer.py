from collections import Counter

def if_contains_anagrams(lst):
    pairs = 0
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    for i in lst:
        i = i.lower()
        if len(i) >= 3:
            count_dict = Counter(i)
            anagram_check = ''.join(english_letters[::-1][:-len(i)].join((count_dict[key] * key for key in count_dict)))
            anagram_check = anagram_check + ''.join(english_letters[-len(i) - 1:].join((count_dict[key] * key for key in count_dict if key not in anagram_check)))
            for j in range(len(lst)):
                if j != lst.index(i):
                    if lst[j].lower() == anagram_check:
                        pairs += 1
                        break
    return pairs <= 66