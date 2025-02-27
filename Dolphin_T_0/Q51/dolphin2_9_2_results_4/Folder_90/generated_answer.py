def if_contains_anagrams(lst):
    count = 0
    total = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if sorted(lst[i].lower()) == sorted(lst[j].lower()) and len(lst[i]) >= 3:
                count += 1
            total += 1
    return count * 2 <= total <= 147