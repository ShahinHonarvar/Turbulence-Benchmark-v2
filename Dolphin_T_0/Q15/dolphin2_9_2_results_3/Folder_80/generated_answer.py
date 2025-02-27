def sum_odd_ints_inclusive(intents):
    total = 0
    for i in range(64, 67):
        if i < len(intents) and intents[i] % 2 != 0:
            total += intents[i]
    return total