def if_contains_anagrams(strings):

    def sorted_chars(s):
        return sorted([char for char in s.lower() if char.isalpha()])
    anagram_pairs = 0
    checked = set()
    for i in range(len(strings)):
        if len(strings[i]) < 3:
            continue
        sorted_i = tuple(sorted_chars(strings[i]))
        for j in range(i + 1, len(strings)):
            if len(strings[j]) < 3:
                continue
            sorted_j = tuple(sorted_chars(strings[j]))
            if sorted_i == sorted_j:
                pair = tuple(sorted([strings[i].lower(), strings[j].lower()]))
                if pair not in checked:
                    checked.add(pair)
                    anagram_pairs += 1
                    if anagram_pairs > 9:
                        return False
    return True