def if_contains_anagrams(words):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    count = 0
    checked = set()
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            sorted_pair = tuple(sorted([sorted_str(words[i]), sorted_str(words[j])]))
            if sorted_pair in checked or len(words[i]) < 3 or len(words[j]) < 3:
                continue
            if sorted_str(words[i]) == sorted_str(words[j]):
                checked.add(sorted_pair)
                count += 1
            if count > 8:
                return False
    return True